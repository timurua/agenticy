from abc import ABC, abstractmethod
import datetime

from enum import Enum
from dataclasses import dataclass

@dataclass
class Message:
    session_id: int
    sequence_id: int
    sequence_number: int
    payload: any

class ActorType(Enum):
    HUMAN = "human"
    AGENT = "agent"
    
class ActorRole(Enum):
    USER = "user"
    SERVICE_PROVIDER = "service_provider"

class ActorChannelMediaType(Enum):
    TEXT = 'text'
    AUDIO = 'audio'
    VIDEO = 'video'
    MIXED = 'mixed'

@dataclass
class Actor(ABC):
    email: str
    type: ActorType
    role: ActorRole
    supported_channel_types: set[ActorChannelMediaType]
    established_channel_types: set[ActorChannelMediaType]
        
    
@dataclass
class ActorText:
    created_at: datetime
    text: str
    
@dataclass
class ActorAudio:
    created_at: datetime
    audio: bytes
    audio_type: str
            
class ActorSession(ABC):
    
    @abstractmethod
    def get_me() -> Actor:
        pass
    
    @abstractmethod
    def get_actors() -> list[Actor]:
        pass
    
    @abstractmethod
    
    
    
    @abstractmethod
    async def get_channel() -> ActorChannel:
        pass
    
    @abstractmethod
    def se() -> list[Actor]:
        pass
    
    
    
    async def 
        

class ActorEngine(ABC):
    """Interface defining the core functionality of an actor system engine."""

    @abstractmethod
    async def connect(self)-> None:
        """Start the actor engine."""
        pass
    
    @abstractmethod
    async def disconnect(self) -> None:
        pass
    
    @abstractmethod
    async def get_session_for_actor(self) -> ActorSession:
        pass
    
    

    @abstractmethod
    def stop(self):
        """Stop the actor engine and cleanup resources."""
        pass

    @abstractmethod
    def create_actor(self, actor_class, *args, **kwargs):
        """Create a new actor instance.
        
        Args:
            actor_class: The class of the actor to create
            *args: Positional arguments to pass to the actor constructor
            **kwargs: Keyword arguments to pass to the actor constructor
        """
        pass

    @abstractmethod
    def send_message(self, recipient, message):
        """Send a message to an actor.
        
        Args:
            recipient: The target actor reference
            message: The message to send
        """
        pass