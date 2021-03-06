/*
 * ML Lab Service
 * Functionality to create and manage Lab projects, services, datasets, models, and experiments.
 *
 * OpenAPI spec version: 2.2.0-SNAPSHOT
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.15
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.MlLabService) {
      root.MlLabService = {};
    }
    root.MlLabService.LabProjectsStatistics = factory(root.MlLabService.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';

  /**
   * The LabProjectsStatistics model module.
   * @module model/LabProjectsStatistics
   * @version 2.2.0-SNAPSHOT
   */

  /**
   * Constructs a new <code>LabProjectsStatistics</code>.
   * @alias module:model/LabProjectsStatistics
   * @class
   */
  var exports = function() {
  };

  /**
   * Constructs a <code>LabProjectsStatistics</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/LabProjectsStatistics} obj Optional instance to populate.
   * @return {module:model/LabProjectsStatistics} The populated <code>LabProjectsStatistics</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('projectsCount'))
        obj.projectsCount = ApiClient.convertToType(data['projectsCount'], 'Number');
      if (data.hasOwnProperty('inactiveProjectsCount'))
        obj.inactiveProjectsCount = ApiClient.convertToType(data['inactiveProjectsCount'], 'Number');
      if (data.hasOwnProperty('sharedProjectsCount'))
        obj.sharedProjectsCount = ApiClient.convertToType(data['sharedProjectsCount'], 'Number');
      if (data.hasOwnProperty('userCount'))
        obj.userCount = ApiClient.convertToType(data['userCount'], 'Number');
      if (data.hasOwnProperty('inactiveUserCount'))
        obj.inactiveUserCount = ApiClient.convertToType(data['inactiveUserCount'], 'Number');
      if (data.hasOwnProperty('jobsCount'))
        obj.jobsCount = ApiClient.convertToType(data['jobsCount'], 'Number');
      if (data.hasOwnProperty('lastModified'))
        obj.lastModified = ApiClient.convertToType(data['lastModified'], 'Number');
      if (data.hasOwnProperty('servicesCount'))
        obj.servicesCount = ApiClient.convertToType(data['servicesCount'], 'Number');
      if (data.hasOwnProperty('filesCount'))
        obj.filesCount = ApiClient.convertToType(data['filesCount'], 'Number');
      if (data.hasOwnProperty('filesTotalSize'))
        obj.filesTotalSize = ApiClient.convertToType(data['filesTotalSize'], 'Number');
      if (data.hasOwnProperty('datasetsCount'))
        obj.datasetsCount = ApiClient.convertToType(data['datasetsCount'], 'Number');
      if (data.hasOwnProperty('datasetsTotalSize'))
        obj.datasetsTotalSize = ApiClient.convertToType(data['datasetsTotalSize'], 'Number');
      if (data.hasOwnProperty('modelsTotalSize'))
        obj.modelsTotalSize = ApiClient.convertToType(data['modelsTotalSize'], 'Number');
      if (data.hasOwnProperty('modelsCount'))
        obj.modelsCount = ApiClient.convertToType(data['modelsCount'], 'Number');
      if (data.hasOwnProperty('serverCount'))
        obj.serverCount = ApiClient.convertToType(data['serverCount'], 'Number');
      if (data.hasOwnProperty('containerCount'))
        obj.containerCount = ApiClient.convertToType(data['containerCount'], 'Number');
      if (data.hasOwnProperty('downloadedFiles'))
        obj.downloadedFiles = ApiClient.convertToType(data['downloadedFiles'], 'Number');
      if (data.hasOwnProperty('experimentsCount'))
        obj.experimentsCount = ApiClient.convertToType(data['experimentsCount'], 'Number');
      if (data.hasOwnProperty('cacheUpdateDate'))
        obj.cacheUpdateDate = ApiClient.convertToType(data['cacheUpdateDate'], 'Number');
      if (data.hasOwnProperty('cacheUpdateDuration'))
        obj.cacheUpdateDuration = ApiClient.convertToType(data['cacheUpdateDuration'], 'Number');
    }
    return obj;
  }

  /**
   * @member {Number} projectsCount
   */
  exports.prototype.projectsCount = undefined;

  /**
   * @member {Number} inactiveProjectsCount
   */
  exports.prototype.inactiveProjectsCount = undefined;

  /**
   * @member {Number} sharedProjectsCount
   */
  exports.prototype.sharedProjectsCount = undefined;

  /**
   * @member {Number} userCount
   */
  exports.prototype.userCount = undefined;

  /**
   * @member {Number} inactiveUserCount
   */
  exports.prototype.inactiveUserCount = undefined;

  /**
   * @member {Number} jobsCount
   */
  exports.prototype.jobsCount = undefined;

  /**
   * @member {Number} lastModified
   */
  exports.prototype.lastModified = undefined;

  /**
   * @member {Number} servicesCount
   */
  exports.prototype.servicesCount = undefined;

  /**
   * @member {Number} filesCount
   */
  exports.prototype.filesCount = undefined;

  /**
   * @member {Number} filesTotalSize
   */
  exports.prototype.filesTotalSize = undefined;

  /**
   * @member {Number} datasetsCount
   */
  exports.prototype.datasetsCount = undefined;

  /**
   * @member {Number} datasetsTotalSize
   */
  exports.prototype.datasetsTotalSize = undefined;

  /**
   * @member {Number} modelsTotalSize
   */
  exports.prototype.modelsTotalSize = undefined;

  /**
   * @member {Number} modelsCount
   */
  exports.prototype.modelsCount = undefined;

  /**
   * @member {Number} serverCount
   */
  exports.prototype.serverCount = undefined;

  /**
   * @member {Number} containerCount
   */
  exports.prototype.containerCount = undefined;

  /**
   * @member {Number} downloadedFiles
   */
  exports.prototype.downloadedFiles = undefined;

  /**
   * @member {Number} experimentsCount
   */
  exports.prototype.experimentsCount = undefined;

  /**
   * @member {Number} cacheUpdateDate
   */
  exports.prototype.cacheUpdateDate = undefined;

  /**
   * @member {Number} cacheUpdateDuration
   */
  exports.prototype.cacheUpdateDuration = undefined;

  return exports;

}));
