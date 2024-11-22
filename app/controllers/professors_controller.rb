class ProfessorsController < ApplicationController
    def index
      @professors = Professor.all
      @current_user = Student.find_by(id: session[:student_id]) if session[:student_id]
    end
  
    def show
      @professor = Professor.find(params[:id])
      @reviews = @professor.reviews
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
      if params[:query].present?
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
  end
  