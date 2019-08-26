# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def is_full(self):
        return len(self.finish_time) == self.size

    def process(self, request):
        if not self.finish_time:
            # finish_time is empty
            cur_finish_time = request.arrived_at + request.time_to_process
            self.finish_time.append(cur_finish_time)
            return Response(False, request.arrived_at)
        else:
            last_packet_finish_time = self.finish_time[-1]

            # pop from the front of finish_time all the packets which are already
            # processed by the time new packet arrives.
            while self.finish_time and self.finish_time[0] <= request.arrived_at:
                del self.finish_time[0]

            if self.is_full():
                return Response(True, -1)

            cur_finish_time = last_packet_finish_time + request.time_to_process
            self.finish_time.append(cur_finish_time)

            return Response(False, last_packet_finish_time)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
