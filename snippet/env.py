class Env(object):
  """The main OpenAI Gym class.
  """

  def step(self, action):
    """Run one timestep of the environment's dynamics.
       Returns observation, reward, done and info.
    """
    raise NotImplementedError

  def reset(self):
    """Resets the state of the environment and returns an initial observation.
    """
    raise NotImplementedError

  def render(self, mode='human'):
    """Renders the environment."""
    raise NotImplementedError

  def seed(self, seed=None):
    """Sets the seed for this env's random number generator(s)."""
    logger.warn("Could not seed environment %s", self)
    return
