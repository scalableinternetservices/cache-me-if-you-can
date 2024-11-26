class ProfessorsController < ApplicationController
  before_action :show_user, only: [:index, :search]
    def index
      @professors = Professor.all
    end
  
    def show
      @professor = Professor.find(params[:id])
      @reviews = @professor.reviews

      if @reviews.any?
        aggregate_rating = @reviews.sum(:rating)
        count = @reviews.count
        @average_rating = (aggregate_rating.to_f / count).round(2)
      else
        @average_rating = nil
      end
    end
  
    def new
      @professor = Professor.new
    end
  
    def create
      @professor = Professor.new(professor_params)
      if @professor.save
        redirect_to professors_path, notice: 'Professor was successfully created.'
      else
        render :new
      end
    end

    def search
      if params[:query].present? and params[:query].length > 0
        @professors = Professor.where("name LIKE ?", "%#{params[:query]}%")
      else
        @professors = Professor.all
      end

      render :index
    end
  
    private
  
    def professor_params
      params.require(:professor).permit(:name, :department)
    end

    def show_user
      @current_user = Student.find_by(id: session[:student_id]) if session[:student_id]
    end
  end
  