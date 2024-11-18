class CreateReviews < ActiveRecord::Migration[7.1]
  def change
    create_table :reviews do |t|
      t.text :content
      t.integer :rating
      t.references :student, null: false, foreign_key: true
      t.references :professor, null: false, foreign_key: true

      t.timestamps
    end
  end
end
