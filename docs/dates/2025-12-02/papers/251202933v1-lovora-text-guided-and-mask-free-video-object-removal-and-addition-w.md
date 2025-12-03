---
layout: default
title: LoVoRA: Text-guided and Mask-free Video Object Removal and Addition with Learnable Object-aware Localization
---

# LoVoRA: Text-guided and Mask-free Video Object Removal and Addition with Learnable Object-aware Localization
**arXiv**：[2512.02933v1](https://arxiv.org/abs/2512.02933) · [PDF](https://arxiv.org/pdf/2512.02933.pdf)  
**作者**：Zhihan Xiao, Lin Liu, Yixin Gao, Xiaopeng Zhang, Haoxuan Che, Songping Mai, Qi Tian  

**一句话要点**：提出LoVoRA框架，通过可学习对象感知定位实现无掩码文本引导视频对象移除与添加

**关键词**：文本引导视频编辑, 对象移除与添加, 可学习对象感知定位, 扩散掩码预测器, 时空一致性, 端到端视频编辑

## 3 点简述
- 核心问题：文本引导视频编辑需时空一致性，现有方法依赖掩码或参考图像，限制泛化能力
- 方法要点：采用可学习对象感知定位机制，结合扩散掩码预测器，实现端到端无外部控制信号编辑
- 实验或效果：通过大量实验和人工评估，验证了LoVoRA的有效性和高质量性能

## 摘要（原文）

> Text-guided video editing, particularly for object removal and addition, remains a challenging task due to the need for precise spatial and temporal consistency. Existing methods often rely on auxiliary masks or reference images for editing guidance, which limits their scalability and generalization. To address these issues, we propose LoVoRA, a novel framework for mask-free video object removal and addition using object-aware localization mechanism. Our approach utilizes a unique dataset construction pipeline that integrates image-to-video translation, optical flow-based mask propagation, and video inpainting, enabling temporally consistent edits. The core innovation of LoVoRA is its learnable object-aware localization mechanism, which provides dense spatio-temporal supervision for both object insertion and removal tasks. By leveraging a Diffusion Mask Predictor, LoVoRA achieves end-to-end video editing without requiring external control signals during inference. Extensive experiments and human evaluation demonstrate the effectiveness and high-quality performance of LoVoRA.

