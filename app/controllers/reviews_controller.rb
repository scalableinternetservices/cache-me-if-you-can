class ReviewsController < ApplicationController
    before_action :set_professor, only: [:new, :create]

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
end
