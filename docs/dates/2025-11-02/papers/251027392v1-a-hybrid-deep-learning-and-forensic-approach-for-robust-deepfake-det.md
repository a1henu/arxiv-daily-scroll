---
layout: default
title: A Hybrid Deep Learning and Forensic Approach for Robust Deepfake Detection
---

# A Hybrid Deep Learning and Forensic Approach for Robust Deepfake Detection
**arXiv**：[2510.27392v1](https://arxiv.org/abs/2510.27392) · [PDF](https://arxiv.org/pdf/2510.27392.pdf)  
**作者**：Sales Aribe Jr  

**一句话要点**：提出融合深度学习和法证特征的混合框架以提升深度伪造检测的鲁棒性和可解释性

**关键词**：深度伪造检测, 混合框架, 法证特征, 深度学习, 鲁棒性, 可解释性

## 3 点简述
- 核心问题：生成对抗网络和扩散模型使合成媒体更逼真，现有检测方法泛化差或对新攻击有限。
- 方法要点：结合噪声残差、JPEG压缩痕迹等法证特征与CNN和ViT的深度学习表示。
- 实验或效果：在多个数据集上F1分数达0.96、0.82和0.77，鲁棒性测试显示压缩和扰动下性能稳定。

## 摘要（原文）

> The rapid evolution of generative adversarial networks (GANs) and diffusion
> models has made synthetic media increasingly realistic, raising societal
> concerns around misinformation, identity fraud, and digital trust. Existing
> deepfake detection methods either rely on deep learning, which suffers from
> poor generalization and vulnerability to distortions, or forensic analysis,
> which is interpretable but limited against new manipulation techniques. This
> study proposes a hybrid framework that fuses forensic features, including noise
> residuals, JPEG compression traces, and frequency-domain descriptors, with deep
> learning representations from convolutional neural networks (CNNs) and vision
> transformers (ViTs). Evaluated on benchmark datasets (FaceForensics++, Celeb-DF
> v2, DFDC), the proposed model consistently outperformed single-method baselines
> and demonstrated superior performance compared to existing state-of-the-art
> hybrid approaches, achieving F1-scores of 0.96, 0.82, and 0.77, respectively.
> Robustness tests demonstrated stable performance under compression (F1 = 0.87
> at QF = 50), adversarial perturbations (AUC = 0.84), and unseen manipulations
> (F1 = 0.79). Importantly, explainability analysis showed that Grad-CAM and
> forensic heatmaps overlapped with ground-truth manipulated regions in 82
> percent of cases, enhancing transparency and user trust. These findings confirm
> that hybrid approaches provide a balanced solution, combining the adaptability
> of deep models with the interpretability of forensic cues, to develop resilient
> and trustworthy deepfake detection systems.

