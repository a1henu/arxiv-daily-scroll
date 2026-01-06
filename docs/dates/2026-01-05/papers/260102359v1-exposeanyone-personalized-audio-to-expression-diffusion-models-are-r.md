---
layout: default
title: ExposeAnyone: Personalized Audio-to-Expression Diffusion Models Are Robust Zero-Shot Face Forgery Detectors
---

# ExposeAnyone: Personalized Audio-to-Expression Diffusion Models Are Robust Zero-Shot Face Forgery Detectors
**arXiv**：[2601.02359v1](https://arxiv.org/abs/2601.02359) · [PDF](https://arxiv.org/pdf/2601.02359.pdf)  
**作者**：Kaede Shiohara, Toshihiko Yamasaki, Vladislav Golyanik  

**一句话要点**：提出ExposeAnyone，基于音频到表情扩散模型，实现零样本人脸伪造检测

**关键词**：人脸伪造检测, 扩散模型, 自监督学习, 零样本学习, 音频到表情生成, 身份距离计算

## 3 点简述
- 核心问题：现有方法难以泛化至未知伪造模式，依赖监督训练导致过拟合
- 方法要点：使用自监督扩散模型，个性化后通过重建误差计算身份距离进行检测
- 实验或效果：在多个数据集上AUC平均提升4.22%，能检测Sora2生成视频，对模糊和压缩鲁棒

## 摘要（原文）

> Detecting unknown deepfake manipulations remains one of the most challenging problems in face forgery detection. Current state-of-the-art approaches fail to generalize to unseen manipulations, as they primarily rely on supervised training with existing deepfakes or pseudo-fakes, which leads to overfitting to specific forgery patterns. In contrast, self-supervised methods offer greater potential for generalization, but existing work struggles to learn discriminative representations only from self-supervision. In this paper, we propose ExposeAnyone, a fully self-supervised approach based on a diffusion model that generates expression sequences from audio. The key idea is, once the model is personalized to specific subjects using reference sets, it can compute the identity distances between suspected videos and personalized subjects via diffusion reconstruction errors, enabling person-of-interest face forgery detection. Extensive experiments demonstrate that 1) our method outperforms the previous state-of-the-art method by 4.22 percentage points in the average AUC on DF-TIMIT, DFDCP, KoDF, and IDForge datasets, 2) our model is also capable of detecting Sora2-generated videos, where the previous approaches perform poorly, and 3) our method is highly robust to corruptions such as blur and compression, highlighting the applicability in real-world face forgery detection.

