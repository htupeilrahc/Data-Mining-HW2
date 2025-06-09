export CUDA_VISIBLE_DEVICES=0

for i in 1 2 3 4 5
do
  python -u run.py \
    --task_name anomaly_detection \
    --is_training 1 \
    --root_path ./dataset/Tube_atleastone_10f/tube$i \
    --model_id tube${i}_atleastone_10f \
    --model FEDformer \
    --data PSM \
    --features M \
    --seq_len 100 \
    --pred_len 0 \
    --d_model 64 \
    --d_ff 64 \
    --e_layers 2 \
    --enc_in 10 \
    --c_out 10 \
    --anomaly_ratio 1 \
    --batch_size 128 \
    --train_epochs 3
done
