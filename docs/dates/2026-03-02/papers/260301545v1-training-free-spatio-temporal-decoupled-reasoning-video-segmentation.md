---
layout: default
title: Training-Free Spatio-temporal Decoupled Reasoning Video Segmentation with Adaptive Object Memory
---

# Training-Free Spatio-temporal Decoupled Reasoning Video Segmentation with Adaptive Object Memory
**arXiv**：[2603.01545v1](https://arxiv.org/abs/2603.01545) · [PDF](https://arxiv.org/pdf/2603.01545.pdf)  
**作者**：Zhengtong Zhu, Jiaqing Fan, Zhixuan Liu, Fanzhang Li  

**一句话要点**：提出无需训练的时空解耦推理视频分割方法SDAM，利用自适应对象记忆提升分割稳定性。

**关键词**：推理视频分割, 无需训练, 时空解耦, 自适应记忆, 多模态大语言模型

## 3 点简述
- 核心问题：推理视频分割任务需稳定分割，现有方法依赖微调且时空耦合影响稳定性。
- 方法要点：设计无需训练框架，通过自适应对象记忆模块选择关键对象，时空解耦实现精准定位与稳定传播。
- 实验或效果：在五个基准数据集上取得优异结果，超越需微调的方法。

## 摘要（原文）

> Reasoning Video Object Segmentation (ReasonVOS) is a challenging task that requires stable object segmentation across video sequences using implicit and complex textual inputs. Previous methods fine-tune Multimodal Large Language Models (MLLMs) to produce segmentation outputs, which demand substantial resources. Additionally, some existing methods are coupled in the processing of spatio-temporal information, which affects the temporal stability of the model to some extent. To address these issues, we propose Training-Free \textbf{S}patio-temporal \textbf{D}ecoupled Reasoning Video Segmentation with \textbf{A}daptive Object \textbf{M}emory (SDAM). We aim to design a training-free reasoning video segmentation framework that outperforms existing methods requiring fine-tuning, using only pre-trained models. Meanwhile, we propose an Adaptive Object Memory module that selects and memorizes key objects based on motion cues in different video sequences. Finally, we propose Spatio-temporal Decoupling for stable temporal propagation. In the spatial domain, we achieve precise localization and segmentation of target objects, while in the temporal domain, we leverage key object temporal information to drive stable cross-frame propagation. Our method achieves excellent results on five benchmark datasets, including Ref-YouTubeVOS, Ref-DAVIS17, MeViS, ReasonVOS, and ReVOS.

