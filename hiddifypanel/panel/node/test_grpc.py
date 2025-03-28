# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: hiddifypanel/async/node/test.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import hiddifypanel.hasync.node.test_pb2


class HelloBase(abc.ABC):

    @abc.abstractmethod
    async def SayHello(self, stream: 'grpclib.server.Stream[hiddifypanel.hasync.node.test_pb2.HelloRequest, hiddifypanel.hasync.node.test_pb2.HelloResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/Hello/SayHello': grpclib.const.Handler(
                self.SayHello,
                grpclib.const.Cardinality.UNARY_UNARY,
                hiddifypanel.hasync.node.test_pb2.HelloRequest,
                hiddifypanel.hasync.node.test_pb2.HelloResponse,
            ),
        }


class HelloStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SayHello = grpclib.client.UnaryUnaryMethod(
            channel,
            '/Hello/SayHello',
            hiddifypanel.hasync.node.test_pb2.HelloRequest,
            hiddifypanel.hasync.node.test_pb2.HelloResponse,
        )
