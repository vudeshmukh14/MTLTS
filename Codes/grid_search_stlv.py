import os

lr_list = [5e-6, 1e-5, 2e-5, 5e-5]

for lr in lr_list:
	os.system(f'python stlv_final.py --lr {lr} --l2 n --test_file charlie > charlie1_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 n --loss_fn w --test_file charlie > charlie2_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 y --wd 0.1 --test_file charlie > charlie3_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 y --wd 0.1 --loss_fn w --test_file charlie > charlie4_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 y --test_file charlie > charlie5_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 y --loss_fn w --test_file charlie > charlie6_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 y --wd 0.001 --test_file charlie > charlie7_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 y --wd 0.001 --loss_fn w --test_file charlie > charlie8_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 n --test_file ottawa > ottawa1_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 n --loss_fn w --test_file ottawa > ottawa2_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 y --wd 0.1 --test_file ottawa > ottawa3_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 y --wd 0.1 --loss_fn w --test_file ottawa > ottawa4_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 y --test_file ottawa > ottawa5_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 y --loss_fn w --test_file ottawa > ottawa6_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 y --wd 0.001 --test_file ottawa > ottawa7_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --l2 y --wd 0.001 --loss_fn w --test_file ottawa > ottawa8_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 n --test_file german > german1_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 n --loss_fn w --test_file german > german2_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --wd 0.1 --test_file german > german3_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --wd 0.1 --loss_fn w --test_file german > german4_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --test_file german > german5_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --loss_fn w --test_file german > german6_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --wd 0.001 --test_file german > german7_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --wd 0.001 --loss_fn w --test_file german > german8_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 n --test_file sydney > sydney1_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 n --loss_fn w --test_file sydney > sydney2_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --wd 0.1 --test_file sydney > sydney3_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --wd 0.1 --loss_fn w --test_file sydney > sydney4_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --test_file sydney > sydney5_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --loss_fn w --test_file sydney > sydney6_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --wd 0.001 --test_file sydney > sydney7_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --wd 0.001 --loss_fn w --test_file sydney > sydney8_{lr}.txt')
	'''
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 n --test_file ferguson > ferguson1_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 n --loss_fn w --test_file ferguson > ferguson2_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --wd 0.1 --test_file ferguson > ferguson3_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --wd 0.1 --loss_fn w --test_file ferguson > ferguson4_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --test_file ferguson > ferguson5_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --loss_fn w --test_file ferguson > ferguson6_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --wd 0.001 --test_file ferguson > ferguson7_{lr}.txt')
	os.system(f'python stlv_final.py --lr {lr} --gpu_id 1 --l2 y --wd 0.001 --loss_fn w --test_file ferguson > ferguson8_{lr}.txt')
	'''