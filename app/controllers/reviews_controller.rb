class ReviewsController < ApplicationController
    before_action :set_professor, only: [:new, :create]
    before_action :authenticate_user!, only: [:new, :create]

    def new
        @review = @professor.reviews.build
        @courses = Course.all
        @current_user = Student.find_by(id: session[:student_id]) if session[:student_id]
    end

    def create
        @review = @professor.reviews.build(review_params)
        @review.student_id = session[:student_id]
        if @review.save
            redirect_to professor_path(@professor), notice: 'Review created successfully.'
        else
            @courses = Course.all
            render :new
        end
    end

    private

    def set_professor
        @professor = Professor.find(params[:professor_id])
    end

    def review_params
        params.require(:review).permit(:content, :rating, :professor_id, :course_id)
    end

    def authenticate_user!
        unless session[:student_id]
            redirect_to login_path, alert: 'You need to log in to create a review.'
        end
    end
end

