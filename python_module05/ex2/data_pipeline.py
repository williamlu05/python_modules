from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._elements: list[str] = []
        self._rank = 0
        self._total = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._elements:
            raise Exception("No data left to output")
        self._rank += 1
        return (self._rank - 1, self._elements.pop(0))

    def total(self) -> int:
        return self._total

    def data(self) -> list[str]:
        return self._elements


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        elif isinstance(data, (int, float)):
            self._elements.append(str(data))
            self._total += 1
        else:
            for number in data:
                self._elements.append(str(number))
                self._total += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        elif isinstance(data, str):
            self._elements.append(data)
            self._total += 1
        else:
            for string in data:
                self._elements.append(string)
                self._total += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return (set(data.keys()) == {"log_level", "log_message"}
                    and all(isinstance(v, str) for v in data.values()))
        elif isinstance(data, list):
            return all(self.validate(x) for x in data)
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        elif isinstance(data, dict):
            self._elements.append(
                f"{data['log_level']}: {data['log_message']}")
            self._total += 1

        else:
            for log in data:
                self._elements.append(
                    f"{log['log_level']}: {log['log_message']}")
                self._total += 1


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value for _, value in data))


class JSONExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        pairs: list[str] = []
        for rank, value in data:
            pairs.append(f'"item_{rank}": "{value}"')
        print("{" + ", ".join(pairs) + "}")


class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            i = 0
            while i < len(self._processors):
                if self._processors[i].validate(element) is True:
                    break
                i += 1

            if i == len(self._processors):
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {element}"
                )
                continue
            try:
                self._processors[i].ingest(element)
            except Exception as e:
                print(f"DataStream error - {e}")

    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===")
        if not self._processors:
            print("No processor found, no data")
        else:
            for processor in self._processors:
                print(
                    f"{type(processor).__name__}:",
                    f"total {processor.total()} items processed,",
                    f"remaining {len(processor.data())} on processor"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            data: list[tuple[int, str]] = []
            while len(data) < nb and processor.data():
                data.append(processor.output())
            plugin.process_output(data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors\n")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()

    batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"\nSend another batch of data: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
