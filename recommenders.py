"""
Here lives our movie recommenders functions
"""
import random
from utils import MOVIES, nmf_model, cosim_model

def nmf_recommender(query:dict, model=nmf_model, k=10) -> list:
    """recommender based on nmf model

    Args:
        query (dict): _description_
        model (_type_): _description_
        k (int, optional): _description_. Defaults to 10.

    Returns:
        list: topk movies
    """
    return NotImplemented


def cosim_recommender(query:dict, model=cosim_model, k=10) -> list:
    """_summary_

    Args:
        query (dict): user query
        model (_type_): _description_
        k (int, optional): _description_. Defaults to 10.

    Returns:
        list: topk movies
    """
    return NotImplemented


def random_recommender(query={"Toy Story": 5}, k=3):
    """Toy random recommender

    Args:
        query (dict, optional): User query. Defaults to {"Toy Story": 5}.
        k (int, optional): _description_. Defaults to 3.

    Returns:
        _type_: _description_
    """
    if k > len(MOVIES):
        print(f"Hey you cannot exceed the {len(MOVIES)} movies")
        return []
    else:
        random.shuffle(MOVIES)
        topk = MOVIES[:k]
        return topk


if __name__ == "__main__":
   top3 =  random_recommender()
   print(top3)