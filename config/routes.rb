Rails.application.routes.draw do
  root "professors#index"
  resources :professors do
    resources :reviews, only: [:new, :create]
  end
  resources :students do
    resources :reviews, only: [:index]
    resources :comments, only: [:index, :new, :create]
  end
  resources :reviews, only: [:show, :edit, :update, :destroy] do
    resources :comments, only: [:index, :create]
  end
  resources :courses
  
  get "login", to: "sessions#new"
  post "login", to: "sessions#create"
  delete "logout", to: "sessions#destroy"
  get "search", to: "professors#search"
  get "professors/index"
end
