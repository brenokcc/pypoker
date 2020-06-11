from poker import GameSubscriber, GameServerRedis, GameRoomFactory, HoldemPokerGameFactory
import logging
import redis
import os


class CustomGameSubscriber(GameSubscriber):

    def game_event(self, event, event_data):
        print(event, event_data)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG if 'DEBUG' in os.environ else logging.INFO)
    logger = logging.getLogger()

    redis = redis.from_url('127.0. 0.1:6379')

    server = GameServerRedis(
        redis=redis,
        connection_channel="texas-holdem-poker:lobby",
        room_factory=GameRoomFactory(
            room_size=10,
            game_factory=HoldemPokerGameFactory(
                big_blind=40.0,
                small_blind=20.0,
                logger=logger,
                game_subscribers=[
                    CustomGameSubscriber()
                ]
            )
        ),
        logger=logger
    )
    server.start()
