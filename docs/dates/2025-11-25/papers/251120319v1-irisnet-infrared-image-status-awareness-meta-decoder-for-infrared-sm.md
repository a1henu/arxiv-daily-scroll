---
layout: default
title: IrisNet: Infrared Image Status Awareness Meta Decoder for Infrared Small Targets Detection
---

# IrisNet: Infrared Image Status Awareness Meta Decoder for Infrared Small Targets Detection
**arXiv**：[2511.20319v1](https://arxiv.org/abs/2511.20319) · [PDF](https://arxiv.org/pdf/2511.20319.pdf)  
**作者**：Xuelin Qian, Jiaming Lu, Zixuan Wang, Wenxuan Wang, Zhongling Huang, Dingwen Zhang, Junwei Han  

**一句话要点**：提出IrisNet动态适应红外图像状态以解决红外小目标检测的鲁棒性问题

**关键词**：红外小目标检测, 元学习, 变换器, 动态解码器, 高频组件

## 3 点简述
- 红外小目标检测面临低信噪比、复杂背景和特征缺失等挑战
- 采用元学习框架，通过图像到解码器变换器动态生成解码器参数
- 在多个数据集上实现最先进性能，验证了方法的优越性

## 摘要（原文）

> Infrared Small Target Detection (IRSTD) faces significant challenges due to low signal-to-noise ratios, complex backgrounds, and the absence of discernible target features. While deep learning-based encoder-decoder frameworks have advanced the field, their static pattern learning suffers from pattern drift across diverse scenarios (\emph{e.g.}, day/night variations, sky/maritime/ground domains), limiting robustness. To address this, we propose IrisNet, a novel meta-learned framework that dynamically adapts detection strategies to the input infrared image status. Our approach establishes a dynamic mapping between infrared image features and entire decoder parameters via an image-to-decoder transformer. More concretely, we represent the parameterized decoder as a structured 2D tensor preserving hierarchical layer correlations and enable the transformer to model inter-layer dependencies through self-attention while generating adaptive decoding patterns via cross-attention. To further enhance the perception ability of infrared images, we integrate high-frequency components to supplement target-position and scene-edge information. Experiments on NUDT-SIRST, NUAA-SIRST, and IRSTD-1K datasets demonstrate the superiority of our IrisNet, achieving state-of-the-art performance.

