'use strict';

var recipeControllers = angular.module('recipeControllers',[]);

recipeControllers.controller('ListCtrl', ['$scope', '$http',
  function ($scope, $http) {
    $http.get('api/list/').success(function(data) {
      $scope.phones = data;
    });

  }]);

recipeControllers.controller('DetailCtrl', ['$scope', '$routeParams',
  function($scope, $routeParams) {
    $scope.recipeId = $routeParams.recipeId;
  }]);


console.log(2);