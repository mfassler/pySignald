

.PHONY: lint
lint:
	pep8 --max-line-length=100 *.py
	pep8 --max-line-length=100 handlers/*.py
	pep8 --max-line-length=100 socket_handlers/*.py
	pep8 --max-line-length=100 lib/*.py

.PHONY: protobuf
protobuf:
	protoc --python_out=./protos_compiled/ protos/SubProtocol.proto
	protoc --python_out=./protos_compiled/ protos/IncomingPushMessageSignal.proto
	protoc --python_out=./protos_compiled/ protos/DeviceMessages.proto
	protoc --python_out=./protos_compiled/ protos/WhisperTextProtocol.proto

