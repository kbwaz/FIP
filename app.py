from cache.cache_manager import CacheManager

# Initialize CacheManager
cache_manager = CacheManager()

def get_llm_response(query):
    """
    Function to get response from LLM with caching.
    
    :param query: The input query for the LLM.
    :return: The response from the LLM.
    """
    # Check if the response is already in the cache
    cached_response = cache_manager.get(query)
    if cached_response:
        print("Cache hit: Returning cached response.")
        return cached_response
    
    # Simulate an LLM request (replace this with actual LLM request logic)
    print("Cache miss: Fetching new response from LLM.")
    response = simulate_llm_request(query)
    
    # Store the new response in the cache
    cache_manager.set(query, response)
    
    return response

def simulate_llm_request(query):
    """
    Simulate an LLM request. Replace this with actual LLM request logic.
    
    :param query: The input query for the LLM.
    :return: Simulated response from the LLM.
    """
    # Simulated response (replace with actual LLM call)
    return f"Response for '{query}'"

if __name__ == "__main__":
    # Example usage
    query = "What is the capital of France?"
    response = get_llm_response(query)
    print(response)
    
    # Fetching the same query again to demonstrate caching
    response = get_llm_response(query)
    print(response)

