---
layout: default
title: Dynamic Training-Free Fusion of Subject and Style LoRAs
---

# Dynamic Training-Free Fusion of Subject and Style LoRAs
**arXiv**：[2602.15539v1](https://arxiv.org/abs/2602.15539) · [PDF](https://arxiv.org/pdf/2602.15539.pdf)  
**作者**：Qinglong Cao, Yuntian Chen, Chao Ma, Xiaokang Yang  

**一句话要点**：提出动态无训练融合框架，通过特征级选择和度量引导调整实现主题与风格LoRA的连贯合成。

**关键词**：LoRA融合, 动态融合, 训练免费成, 扩散模型, 主题风格合成

## 3 点简述
- 现有方法静态融合LoRA权重，偏离自适应调整初衷且忽略输入随机性。
- 在生成过程中动态计算KL散度选择权重，并基于CLIP/DINO分数进行梯度校正。
- 实验表明，该方法在多样主题-风格组合中优于现有方法，无需重训练。

## 摘要（原文）

> Recent studies have explored the combination of multiple LoRAs to simultaneously generate user-specified subjects and styles. However, most existing approaches fuse LoRA weights using static statistical heuristics that deviate from LoRA's original purpose of learning adaptive feature adjustments and ignore the randomness of sampled inputs. To address this, we propose a dynamic training-free fusion framework that operates throughout the generation process. During the forward pass, at each LoRA-applied layer, we dynamically compute the KL divergence between the base model's original features and those produced by subject and style LoRAs, respectively, and adaptively select the most appropriate weights for fusion. In the reverse denoising stage, we further refine the generation trajectory by dynamically applying gradient-based corrections derived from objective metrics such as CLIP and DINO scores, providing continuous semantic and stylistic guidance. By integrating these two complementary mechanisms-feature-level selection and metric-guided latent adjustment-across the entire diffusion timeline, our method dynamically achieves coherent subject-style synthesis without any retraining. Extensive experiments across diverse subject-style combinations demonstrate that our approach consistently outperforms state-of-the-art LoRA fusion methods both qualitatively and quantitatively.

