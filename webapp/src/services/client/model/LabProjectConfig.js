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
    root.MlLabService.LabProjectConfig = factory(root.MlLabService.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';

  /**
   * The LabProjectConfig model module.
   * @module model/LabProjectConfig
   * @version 2.2.0-SNAPSHOT
   */

  /**
   * Constructs a new <code>LabProjectConfig</code>.
   * @alias module:model/LabProjectConfig
   * @class
   */
  var exports = function() {
  };

  /**
   * Constructs a <code>LabProjectConfig</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/LabProjectConfig} obj Optional instance to populate.
   * @return {module:model/LabProjectConfig} The populated <code>LabProjectConfig</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('name'))
        obj.name = ApiClient.convertToType(data['name'], 'String');
      if (data.hasOwnProperty('description'))
        obj.description = ApiClient.convertToType(data['description'], 'String');
      if (data.hasOwnProperty('visibility'))
        obj.visibility = ApiClient.convertToType(data['visibility'], 'String');
    }
    return obj;
  }

  /**
   * @member {String} name
   */
  exports.prototype.name = undefined;

  /**
   * @member {String} description
   */
  exports.prototype.description = undefined;

  /**
   * @member {String} visibility
   */
  exports.prototype.visibility = undefined;

  return exports;

}));