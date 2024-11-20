Rails.application.routes.draw do
  root "professors#index"
  resources :professors do
    resources :reviews, only: [:new, :create]
  end
  get "search", to: "professors#search", as: "search"
  resources :students do
    resources :reviews, only: [:index]
    resources :comments, only: [:index, :new, :create]
  end
  resources :reviews, only: [:new, :create] do
    resources :comments, only: [:index, :create]
  end
  resources :courses, only: [:new, :create]
  
  get "login", to: "sessions#new"
  post "login", to: "sessions#create"
  delete "logout", to: "sessions#destroy"
  get "search", to: "professors#search"
  get "professors/index"

  
end
