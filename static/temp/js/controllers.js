'use strict';

var recipeControllers = angular.module('recipeControllers',[]);

recipeControllers.controller('ListCtrl', ['$scope', '$http',
  function ($scope, $http) {
    $http.get('api/list/').success(function(data) {
      $scope.items = data;
      console.log(data);
    });

  }]);

recipeControllers.controller('DetailCtrl', ['$scope', '$http','$routeParams',
  function($scope, $http, $routeParams) {
    $http.get('api/det/'+$routeParams.recipeId).success(function(data) {
      $scope.items = data;
      console.log(data);
    });

  }]);


