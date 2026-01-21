---
layout: default
title: VideoMaMa: Mask-Guided Video Matting via Generative Prior
---

# VideoMaMa: Mask-Guided Video Matting via Generative Prior
**arXiv**：[2601.14255v1](https://arxiv.org/abs/2601.14255) · [PDF](https://arxiv.org/pdf/2601.14255.pdf)  
**作者**：Sangbeom Lim, Seoung Wug Oh, Jiahui Huang, Heeji Yoon, Seungryong Kim, Joon-Young Lee  

**一句话要点**：提出VideoMaMa，利用生成先验将粗分割掩码转换为精确alpha遮罩，以解决视频抠图泛化难题。

**关键词**：视频抠图, 生成先验, 零样本泛化, 伪标注数据集, 扩散模型, 掩码引导

## 3 点简述
- 核心问题：视频抠图模型因标注数据稀缺，难以泛化到真实世界视频。
- 方法要点：基于预训练视频扩散模型，通过掩码引导实现零样本泛化，并构建大规模伪标注数据集MA-V。
- 实验或效果：在合成数据上训练，展示强零样本泛化能力；SAM2-Matte在MA-V上微调后，在野外视频中鲁棒性优于现有数据集训练模型。

## 摘要（原文）

> Generalizing video matting models to real-world videos remains a significant challenge due to the scarcity of labeled data. To address this, we present Video Mask-to-Matte Model (VideoMaMa) that converts coarse segmentation masks into pixel accurate alpha mattes, by leveraging pretrained video diffusion models. VideoMaMa demonstrates strong zero-shot generalization to real-world footage, even though it is trained solely on synthetic data. Building on this capability, we develop a scalable pseudo-labeling pipeline for large-scale video matting and construct the Matting Anything in Video (MA-V) dataset, which offers high-quality matting annotations for more than 50K real-world videos spanning diverse scenes and motions. To validate the effectiveness of this dataset, we fine-tune the SAM2 model on MA-V to obtain SAM2-Matte, which outperforms the same model trained on existing matting datasets in terms of robustness on in-the-wild videos. These findings emphasize the importance of large-scale pseudo-labeled video matting and showcase how generative priors and accessible segmentation cues can drive scalable progress in video matting research.

