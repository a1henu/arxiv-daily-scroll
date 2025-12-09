---
layout: default
title: DeepAgent: A Dual Stream Multi Agent Fusion for Robust Multimodal Deepfake Detection
---

# DeepAgent: A Dual Stream Multi Agent Fusion for Robust Multimodal Deepfake Detection
**arXiv**：[2512.07351v1](https://arxiv.org/abs/2512.07351) · [PDF](https://arxiv.org/pdf/2512.07351.pdf)  
**作者**：Sayeem Been Zaman, Wasimul Karim, Arefin Ittesafun Abian, Reem E. Mohamed, Md Rafiqul Islam, Asif Karim, Sami Azam  

**一句话要点**：提出DeepAgent多智能体融合框架，通过双流协作提升多模态深度伪造检测的鲁棒性。

**关键词**：多模态深度伪造检测, 多智能体协作, 视听不一致性检测, 随机森林融合, 跨数据集验证, 鲁棒性增强

## 3 点简述
- 核心问题：现有单模型多模态深度伪造检测易受模态不匹配、噪声和操纵影响，鲁棒性不足。
- 方法要点：设计双智能体协作框架，Agent-1基于AlexNet检测视觉伪造痕迹，Agent-2结合音频特征和OCR检测视听不一致性，通过随机森林元分类器融合决策。
- 实验或效果：在多个基准数据集上验证，元分类器在DeepFakeTIMIT上达到97.49%准确率，显示跨数据集鲁棒性。

## 摘要（原文）

> The increasing use of synthetic media, particularly deepfakes, is an emerging challenge for digital content verification. Although recent studies use both audio and visual information, most integrate these cues within a single model, which remains vulnerable to modality mismatches, noise, and manipulation. To address this gap, we propose DeepAgent, an advanced multi-agent collaboration framework that simultaneously incorporates both visual and audio modalities for the effective detection of deepfakes. DeepAgent consists of two complementary agents. Agent-1 examines each video with a streamlined AlexNet-based CNN to identify the symbols of deepfake manipulation, while Agent-2 detects audio-visual inconsistencies by combining acoustic features, audio transcriptions from Whisper, and frame-reading sequences of images through EasyOCR. Their decisions are fused through a Random Forest meta-classifier that improves final performance by taking advantage of the different decision boundaries learned by each agent. This study evaluates the proposed framework using three benchmark datasets to demonstrate both component-level and fused performance. Agent-1 achieves a test accuracy of 94.35% on the combined Celeb-DF and FakeAVCeleb datasets. On the FakeAVCeleb dataset, Agent-2 and the final meta-classifier attain accuracies of 93.69% and 81.56%, respectively. In addition, cross-dataset validation on DeepFakeTIMIT confirms the robustness of the meta-classifier, which achieves a final accuracy of 97.49%, and indicates a strong capability across diverse datasets. These findings confirm that hierarchy-based fusion enhances robustness by mitigating the weaknesses of individual modalities and demonstrate the effectiveness of a multi-agent approach in addressing diverse types of manipulations in deepfakes.

