import time

class RequestTimeMiddleware:
    """
    Custom middleware to print request path and measure request processing time.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Record start time
        start_time = time.time()

        # Print request path
        print(f"Request Path: {request.path}")

        # Process view
        response = self.get_response(request)

        # Calculate total time
        total_time = time.time() - start_time
        print(f"Time Taken: {total_time:.4f} seconds")

        return response