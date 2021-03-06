# coding: utf-8

"""
    ML Lab Service

    Functionality to create and manage Lab projects, services, datasets, models, and experiments.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LabProjectsStatistics(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'services_count': 'int',
        'files_count': 'int',
        'files_total_size': 'float',
        'projects_count': 'int',
        'inactive_projects_count': 'int',
        'shared_projects_count': 'int',
        'user_count': 'int',
        'inactive_user_count': 'int',
        'jobs_count': 'int',
        'datasets_count': 'int',
        'datasets_total_size': 'float',
        'models_total_size': 'float',
        'models_count': 'int',
        'server_count': 'int',
        'container_count': 'int',
        'downloaded_files': 'int',
        'experiments_count': 'int',
        'cache_update_date': 'int',
        'cache_update_duration': 'int',
        'last_modified': 'int'
    }

    attribute_map = {
        'services_count': 'servicesCount',
        'files_count': 'filesCount',
        'files_total_size': 'filesTotalSize',
        'projects_count': 'projectsCount',
        'inactive_projects_count': 'inactiveProjectsCount',
        'shared_projects_count': 'sharedProjectsCount',
        'user_count': 'userCount',
        'inactive_user_count': 'inactiveUserCount',
        'jobs_count': 'jobsCount',
        'datasets_count': 'datasetsCount',
        'datasets_total_size': 'datasetsTotalSize',
        'models_total_size': 'modelsTotalSize',
        'models_count': 'modelsCount',
        'server_count': 'serverCount',
        'container_count': 'containerCount',
        'downloaded_files': 'downloadedFiles',
        'experiments_count': 'experimentsCount',
        'cache_update_date': 'cacheUpdateDate',
        'cache_update_duration': 'cacheUpdateDuration',
        'last_modified': 'lastModified'
    }

    def __init__(self, services_count=None, files_count=None, files_total_size=None, projects_count=None, inactive_projects_count=None, shared_projects_count=None, user_count=None, inactive_user_count=None, jobs_count=None, datasets_count=None, datasets_total_size=None, models_total_size=None, models_count=None, server_count=None, container_count=None, downloaded_files=None, experiments_count=None, cache_update_date=None, cache_update_duration=None, last_modified=None):  # noqa: E501
        """LabProjectsStatistics - a model defined in Swagger"""  # noqa: E501

        self._services_count = None
        self._files_count = None
        self._files_total_size = None
        self._projects_count = None
        self._inactive_projects_count = None
        self._shared_projects_count = None
        self._user_count = None
        self._inactive_user_count = None
        self._jobs_count = None
        self._datasets_count = None
        self._datasets_total_size = None
        self._models_total_size = None
        self._models_count = None
        self._server_count = None
        self._container_count = None
        self._downloaded_files = None
        self._experiments_count = None
        self._cache_update_date = None
        self._cache_update_duration = None
        self._last_modified = None
        self.discriminator = None

        if services_count is not None:
            self.services_count = services_count
        if files_count is not None:
            self.files_count = files_count
        if files_total_size is not None:
            self.files_total_size = files_total_size
        if projects_count is not None:
            self.projects_count = projects_count
        if inactive_projects_count is not None:
            self.inactive_projects_count = inactive_projects_count
        if shared_projects_count is not None:
            self.shared_projects_count = shared_projects_count
        if user_count is not None:
            self.user_count = user_count
        if inactive_user_count is not None:
            self.inactive_user_count = inactive_user_count
        if jobs_count is not None:
            self.jobs_count = jobs_count
        if datasets_count is not None:
            self.datasets_count = datasets_count
        if datasets_total_size is not None:
            self.datasets_total_size = datasets_total_size
        if models_total_size is not None:
            self.models_total_size = models_total_size
        if models_count is not None:
            self.models_count = models_count
        if server_count is not None:
            self.server_count = server_count
        if container_count is not None:
            self.container_count = container_count
        if downloaded_files is not None:
            self.downloaded_files = downloaded_files
        if experiments_count is not None:
            self.experiments_count = experiments_count
        if cache_update_date is not None:
            self.cache_update_date = cache_update_date
        if cache_update_duration is not None:
            self.cache_update_duration = cache_update_duration
        if last_modified is not None:
            self.last_modified = last_modified

    @property
    def services_count(self):
        """Gets the services_count of this LabProjectsStatistics.  # noqa: E501


        :return: The services_count of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._services_count

    @services_count.setter
    def services_count(self, services_count):
        """Sets the services_count of this LabProjectsStatistics.


        :param services_count: The services_count of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._services_count = services_count

    @property
    def files_count(self):
        """Gets the files_count of this LabProjectsStatistics.  # noqa: E501


        :return: The files_count of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._files_count

    @files_count.setter
    def files_count(self, files_count):
        """Sets the files_count of this LabProjectsStatistics.


        :param files_count: The files_count of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._files_count = files_count

    @property
    def files_total_size(self):
        """Gets the files_total_size of this LabProjectsStatistics.  # noqa: E501


        :return: The files_total_size of this LabProjectsStatistics.  # noqa: E501
        :rtype: float
        """
        return self._files_total_size

    @files_total_size.setter
    def files_total_size(self, files_total_size):
        """Sets the files_total_size of this LabProjectsStatistics.


        :param files_total_size: The files_total_size of this LabProjectsStatistics.  # noqa: E501
        :type: float
        """

        self._files_total_size = files_total_size

    @property
    def projects_count(self):
        """Gets the projects_count of this LabProjectsStatistics.  # noqa: E501


        :return: The projects_count of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._projects_count

    @projects_count.setter
    def projects_count(self, projects_count):
        """Sets the projects_count of this LabProjectsStatistics.


        :param projects_count: The projects_count of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._projects_count = projects_count

    @property
    def inactive_projects_count(self):
        """Gets the inactive_projects_count of this LabProjectsStatistics.  # noqa: E501


        :return: The inactive_projects_count of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._inactive_projects_count

    @inactive_projects_count.setter
    def inactive_projects_count(self, inactive_projects_count):
        """Sets the inactive_projects_count of this LabProjectsStatistics.


        :param inactive_projects_count: The inactive_projects_count of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._inactive_projects_count = inactive_projects_count

    @property
    def shared_projects_count(self):
        """Gets the shared_projects_count of this LabProjectsStatistics.  # noqa: E501


        :return: The shared_projects_count of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._shared_projects_count

    @shared_projects_count.setter
    def shared_projects_count(self, shared_projects_count):
        """Sets the shared_projects_count of this LabProjectsStatistics.


        :param shared_projects_count: The shared_projects_count of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._shared_projects_count = shared_projects_count

    @property
    def user_count(self):
        """Gets the user_count of this LabProjectsStatistics.  # noqa: E501


        :return: The user_count of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this LabProjectsStatistics.


        :param user_count: The user_count of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._user_count = user_count

    @property
    def inactive_user_count(self):
        """Gets the inactive_user_count of this LabProjectsStatistics.  # noqa: E501


        :return: The inactive_user_count of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._inactive_user_count

    @inactive_user_count.setter
    def inactive_user_count(self, inactive_user_count):
        """Sets the inactive_user_count of this LabProjectsStatistics.


        :param inactive_user_count: The inactive_user_count of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._inactive_user_count = inactive_user_count

    @property
    def jobs_count(self):
        """Gets the jobs_count of this LabProjectsStatistics.  # noqa: E501


        :return: The jobs_count of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._jobs_count

    @jobs_count.setter
    def jobs_count(self, jobs_count):
        """Sets the jobs_count of this LabProjectsStatistics.


        :param jobs_count: The jobs_count of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._jobs_count = jobs_count

    @property
    def datasets_count(self):
        """Gets the datasets_count of this LabProjectsStatistics.  # noqa: E501


        :return: The datasets_count of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._datasets_count

    @datasets_count.setter
    def datasets_count(self, datasets_count):
        """Sets the datasets_count of this LabProjectsStatistics.


        :param datasets_count: The datasets_count of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._datasets_count = datasets_count

    @property
    def datasets_total_size(self):
        """Gets the datasets_total_size of this LabProjectsStatistics.  # noqa: E501


        :return: The datasets_total_size of this LabProjectsStatistics.  # noqa: E501
        :rtype: float
        """
        return self._datasets_total_size

    @datasets_total_size.setter
    def datasets_total_size(self, datasets_total_size):
        """Sets the datasets_total_size of this LabProjectsStatistics.


        :param datasets_total_size: The datasets_total_size of this LabProjectsStatistics.  # noqa: E501
        :type: float
        """

        self._datasets_total_size = datasets_total_size

    @property
    def models_total_size(self):
        """Gets the models_total_size of this LabProjectsStatistics.  # noqa: E501


        :return: The models_total_size of this LabProjectsStatistics.  # noqa: E501
        :rtype: float
        """
        return self._models_total_size

    @models_total_size.setter
    def models_total_size(self, models_total_size):
        """Sets the models_total_size of this LabProjectsStatistics.


        :param models_total_size: The models_total_size of this LabProjectsStatistics.  # noqa: E501
        :type: float
        """

        self._models_total_size = models_total_size

    @property
    def models_count(self):
        """Gets the models_count of this LabProjectsStatistics.  # noqa: E501


        :return: The models_count of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._models_count

    @models_count.setter
    def models_count(self, models_count):
        """Sets the models_count of this LabProjectsStatistics.


        :param models_count: The models_count of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._models_count = models_count

    @property
    def server_count(self):
        """Gets the server_count of this LabProjectsStatistics.  # noqa: E501


        :return: The server_count of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._server_count

    @server_count.setter
    def server_count(self, server_count):
        """Sets the server_count of this LabProjectsStatistics.


        :param server_count: The server_count of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._server_count = server_count

    @property
    def container_count(self):
        """Gets the container_count of this LabProjectsStatistics.  # noqa: E501


        :return: The container_count of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._container_count

    @container_count.setter
    def container_count(self, container_count):
        """Sets the container_count of this LabProjectsStatistics.


        :param container_count: The container_count of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._container_count = container_count

    @property
    def downloaded_files(self):
        """Gets the downloaded_files of this LabProjectsStatistics.  # noqa: E501


        :return: The downloaded_files of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._downloaded_files

    @downloaded_files.setter
    def downloaded_files(self, downloaded_files):
        """Sets the downloaded_files of this LabProjectsStatistics.


        :param downloaded_files: The downloaded_files of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._downloaded_files = downloaded_files

    @property
    def experiments_count(self):
        """Gets the experiments_count of this LabProjectsStatistics.  # noqa: E501


        :return: The experiments_count of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._experiments_count

    @experiments_count.setter
    def experiments_count(self, experiments_count):
        """Sets the experiments_count of this LabProjectsStatistics.


        :param experiments_count: The experiments_count of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._experiments_count = experiments_count

    @property
    def cache_update_date(self):
        """Gets the cache_update_date of this LabProjectsStatistics.  # noqa: E501


        :return: The cache_update_date of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._cache_update_date

    @cache_update_date.setter
    def cache_update_date(self, cache_update_date):
        """Sets the cache_update_date of this LabProjectsStatistics.


        :param cache_update_date: The cache_update_date of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._cache_update_date = cache_update_date

    @property
    def cache_update_duration(self):
        """Gets the cache_update_duration of this LabProjectsStatistics.  # noqa: E501


        :return: The cache_update_duration of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._cache_update_duration

    @cache_update_duration.setter
    def cache_update_duration(self, cache_update_duration):
        """Sets the cache_update_duration of this LabProjectsStatistics.


        :param cache_update_duration: The cache_update_duration of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._cache_update_duration = cache_update_duration

    @property
    def last_modified(self):
        """Gets the last_modified of this LabProjectsStatistics.  # noqa: E501


        :return: The last_modified of this LabProjectsStatistics.  # noqa: E501
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this LabProjectsStatistics.


        :param last_modified: The last_modified of this LabProjectsStatistics.  # noqa: E501
        :type: int
        """

        self._last_modified = last_modified

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LabProjectsStatistics, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LabProjectsStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
