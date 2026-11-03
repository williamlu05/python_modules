from abc import ABC, abstractmethod
from typing import Any


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
        for processor in self._processors:
            print(
                f"{type(processor).__name__}:",
                f"total {processor.total()} items processed,",
                f"remaining {len(processor.data())} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor\n")
    numeric = NumericProcessor()
    stream.register_processor(numeric)

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

    print("\nRegistering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    log.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
