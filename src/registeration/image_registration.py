"""This module provides functionalites for giving the option to submit the image for E-ID cards."""

from email.mime import image
from typing import Union
from pathlib import Path
import os
import shutil
import errno
import requests

def get_image_from_local(image_path: Union[str, Path], dest_path: Union[str, Path]) -> str:
    """Submitting image from a local device

    Args:
        image_path (Union[str, Path]): path to the submitting image
        dest_path (Union[str, Path]): path for sotring the image

    Raises:
        FileExistsError: Is raised when a file with the same name exists
        FileNotFoundError: Is raised when the directory for storing the image isn't defined.

    Returns:
        str: the name of the stored file
    """
    # expanding the paths to absolute path
    image_path = os.path.expanduser(image_path)
    dest_path = os.path.expanduser(dest_path)

    if os.path.exists(image_path):  # checking if the image path exists
        if not os.path.exists(dest_path): # checking if a file with the same dest_path exists
            shutil.copyfile(image_path, dest_path)
            return str(dest_path).split("/")[-1]

        else:   # the case of existing a file with the same path as dest_path
            raise FileExistsError(errno.EEXIST, os.strerror(errno.EEXIST), dest_path)
    else:       # the case that image path is not found
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), image_path)

def get_image_from_url(url: str, dest_path: Union[str, Path])-> str:
    """Submitting an image using a url

    Args:
        url (str): The link to the image
        dest_path (Union[str, Path]): Destination path for storing the image

    Raises:
        FileExistsError: Is raised in case a file with the same name is registered.

    Returns:
        str: the name of the stored file
    """
    # expanding the path to absolute path
    dest_path = os.path.expanduser(dest_path)
    # getting the response for url request
    response = requests.get(url, allow_redirects=True)

    if os.path.exists(dest_path):   # checking if a file with the same dest_path exists 
        raise FileExistsError(errno.EEXIST, os.strerror(errno.EEXIST), dest_path) # the case of existing a file with the same path as dest_path
    open(dest_path, "wb").write(response.content) # writing the downloaded image to a file

    return str(dest_path).split("/")[-1]
