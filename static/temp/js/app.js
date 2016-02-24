
 'use strict';

var recipeApp = angular.module('recipeApp', [
  'ngRoute',
  'recipeControllers'
]);

recipeApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        // отображение всех рецептов
        templateUrl: 'static/temp/partials/list.html',
        controller: 'ListCtrl'
      }).
      when('/detail/:recipeId', {
        // По нажатию на рицепт показываются ингредиенты
        templateUrl: 'static/temp/partials/detail.html',
        controller: 'DetailCtrl'
      }).otherwise({
        redirectTo: '/'
      });
  }]);

recipeApp.config([
    '$httpProvider', function($httpProvider) {
      $httpProvider.defaults.xsrfCookieName = 'csrftoke',
      $httpProvider.defaults.xsrfCookieName = 'X-CSRFToken'
  }
]);


 console.log(1);