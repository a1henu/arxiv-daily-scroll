---
layout: default
title: Object-Centric Vision Token Pruning for Vision Language Models
---

# Object-Centric Vision Token Pruning for Vision Language Models
**arXiv**：[2511.20439v1](https://arxiv.org/abs/2511.20439) · [PDF](https://arxiv.org/pdf/2511.20439.pdf)  
**作者**：Guangyuan Li, Rongzhen Zhao, Jinhong Deng, Yanbo Wang, Joni Pajarinen  

**一句话要点**：提出OC-VTP以直接选择代表性视觉令牌，提升视觉语言模型推理效率

**关键词**：视觉语言模型, 令牌剪枝, 对象中心剪枝, 推理效率, 重构误差

## 3 点简述
- 视觉语言模型中视觉令牌数量多但信息分散，导致计算冗余
- OC-VTP通过轻量预训练对象中心剪枝器，最小化重构误差选择令牌
- 实验显示OC-VTP在多种剪枝比下保持最高推理精度，无需微调

## 摘要（原文）

> In Vision Language Models (VLMs), vision tokens are quantity-heavy yet information-dispersed compared with language tokens, thus consume too much unnecessary computation. Pruning redundant vision tokens for high VLM inference efficiency has been continuously studied but all existing methods resort to indirect and non-guaranteed ways. We propose OC-VTP, a direct and guaranteed approach to select the most representative vision tokens for high-efficiency yet accuracy-preserving VLM inference. Our OC-VTP requires merely light-weight pre-training of a small object-centric vision token pruner, which can then be inserted into existing VLMs, without fine-tuning of any models on any datasets. It is gauranteed that the most representative vision tokens are kept by minimizing the error in reconstructing the original unpruned tokens from the selected ones. Across any vision pruning ratios, i.e., inference efficiency, our OC-VTP consistently helps mainstream VLMs to preserve the highest inference accuracy. Our pruning also demonstrates interesting interpretability. Our codes are available at https://github.com/GarryLarry010131/OC-VTP.

