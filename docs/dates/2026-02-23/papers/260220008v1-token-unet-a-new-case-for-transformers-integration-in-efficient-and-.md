---
layout: default
title: Token-UNet: A New Case for Transformers Integration in Efficient and Interpretable 3D UNets for Brain Imaging Segmentation
---

# Token-UNet: A New Case for Transformers Integration in Efficient and Interpretable 3D UNets for Brain Imaging Segmentation
**arXiv**：[2602.20008v1](https://arxiv.org/abs/2602.20008) · [PDF](https://arxiv.org/pdf/2602.20008.pdf)  
**作者**：Louis Fabrice Tshimanga, Andrea Zanola, Federico Del Pup, Manfredo Atzori  

**一句话要点**：提出Token-UNet以在计算受限环境中实现高效可解释的3D脑成像分割

**关键词**：3D医学影像分割, Transformer集成, 计算效率优化, 可解释性注意力, TokenLearner模块, 脑成像分析

## 3 点简述
- 当前3D医学影像分割中Transformer模型因计算复杂度高而难以部署
- Token-UNet结合卷积编码器与TokenLearner模块，从特征图提取预设数量的令牌以降低计算需求
- 实验显示模型在内存、推理时间和参数量上显著减少，同时分割性能略有提升

## 摘要（原文）

> We present Token-UNet, adopting the TokenLearner and TokenFuser modules to encase Transformers into UNets.
>   While Transformers have enabled global interactions among input elements in medical imaging, current computational challenges hinder their deployment on common hardware. Models like (Swin)UNETR adapt the UNet architecture by incorporating (Swin)Transformer encoders, which process tokens that each represent small subvolumes ($8^3$ voxels) of the input.
>   The Transformer attention mechanism scales quadratically with the number of tokens, which is tied to the cubic scaling of 3D input resolution.
>   This work reconsiders the role of convolution and attention, introducing Token-UNets, a family of 3D segmentation models that can operate in constrained computational environments and time frames.
>   To mitigate computational demands, our approach maintains the convolutional encoder of UNet-like models, and applies TokenLearner to 3D feature maps. This module pools a preset number of tokens from local and global structures.
>   Our results show this tokenization effectively encodes task-relevant information, yielding naturally interpretable attention maps. The memory footprint, computation times at inference, and parameter counts of our heaviest model are reduced to 33\%, 10\%, and 35\% of the SwinUNETR values, with better average performance (86.75\% $\pm 0.19\%$ Dice score for SwinUNETR vs our 87.21\% $\pm 0.35\%$).
>   This work opens the way to more efficient trainings in contexts with limited computational resources, such as 3D medical imaging. Easing model optimization, fine-tuning, and transfer-learning in limited hardware settings can accelerate and diversify the development of approaches, for the benefit of the research community.

