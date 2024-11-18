Rails.application.routes.draw do
  root "home#index"
  resources :students, only: [:new, :create]
  get "login", to: "sessions#new"
  post "login", to: "sessions#create"
  delete "logout", to: "sessions#destroy"
  get "search", to: "home#search"
  get "home/index"
end
