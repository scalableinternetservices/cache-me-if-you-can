class CreateProfessors < ActiveRecord::Migration[7.1]
  def change
    create_table :professors do |t|
      t.string :name
      t.string :department

      t.timestamps
    end
  end
end
