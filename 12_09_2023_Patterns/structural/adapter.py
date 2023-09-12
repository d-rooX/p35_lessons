# Legacy class with an incompatible interface
class LegacyLogger:
    def log_message_to_file(self, message):
        print(f"Legacy Logging: {message}")

# Modern logging framework with a different interface
class ModernLogger:
    def log(self, message):
        print(f"Modern Logging: {message}")

# Adapter to make the LegacyLogger compatible with the ModernLogger interface
class LegacyLoggerAdapter(ModernLogger):
    def __init__(self, legacy_logger):
        self.legacy_logger = legacy_logger

    def log(self, message):
        self.legacy_logger.log_message_to_file(message)

# Function that logs messages using the ModernLogger interface
def log_messages(logger, messages):
    for message in messages:
        logger.log(message)

# Usage example
if __name__ == "__main__":
    legacy_logger = LegacyLogger()
    modern_logger = ModernLogger()

    # Log messages using the modern logger directly
    log_messages(modern_logger, ["Message 1", "Message 2"])

    # Use the adapter to log messages using the legacy logger
    legacy_adapter = LegacyLoggerAdapter(legacy_logger)
    log_messages(legacy_adapter, ["Message 3", "Message 4"])
