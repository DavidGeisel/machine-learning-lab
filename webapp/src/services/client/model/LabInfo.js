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
    root.MlLabService.LabInfo = factory(root.MlLabService.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';

  /**
   * The LabInfo model module.
   * @module model/LabInfo
   * @version 2.2.0-SNAPSHOT
   */

  /**
   * Constructs a new <code>LabInfo</code>.
   * @alias module:model/LabInfo
   * @class
   */
  var exports = function() {
  };

  /**
   * Constructs a <code>LabInfo</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/LabInfo} obj Optional instance to populate.
   * @return {module:model/LabInfo} The populated <code>LabInfo</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('version'))
        obj.version = ApiClient.convertToType(data['version'], 'String');
      if (data.hasOwnProperty('runtime'))
        obj.runtime = ApiClient.convertToType(data['runtime'], 'String');
      if (data.hasOwnProperty('namespace'))
        obj.namespace = ApiClient.convertToType(data['namespace'], 'String');
      if (data.hasOwnProperty('projectsCount'))
        obj.projectsCount = ApiClient.convertToType(data['projectsCount'], 'Number');
      if (data.hasOwnProperty('termsOfService'))
        obj.termsOfService = ApiClient.convertToType(data['termsOfService'], 'String');
      if (data.hasOwnProperty('coreServiceInfo'))
        obj.coreServiceInfo = ApiClient.convertToType(data['coreServiceInfo'], {'String': 'String'});
      if (data.hasOwnProperty('healthy'))
        obj.healthy = ApiClient.convertToType(data['healthy'], 'Boolean');
    }
    return obj;
  }

  /**
   * @member {String} version
   */
  exports.prototype.version = undefined;

  /**
   * @member {String} runtime
   */
  exports.prototype.runtime = undefined;

  /**
   * @member {String} namespace
   */
  exports.prototype.namespace = undefined;

  /**
   * @member {Number} projectsCount
   */
  exports.prototype.projectsCount = undefined;

  /**
   * @member {String} termsOfService
   */
  exports.prototype.termsOfService = undefined;

  /**
   * @member {Object.<String, String>} coreServiceInfo
   */
  exports.prototype.coreServiceInfo = undefined;

  /**
   * @member {Boolean} healthy
   */
  exports.prototype.healthy = undefined;

  return exports;

}));
