---
layout: default
title: Leveraging Multimodal LLM Descriptions of Activity for Explainable Semi-Supervised Video Anomaly Detection
---

# Leveraging Multimodal LLM Descriptions of Activity for Explainable Semi-Supervised Video Anomaly Detection
**arXiv**：[2510.14896v1](https://arxiv.org/abs/2510.14896) · [PDF](https://arxiv.org/pdf/2510.14896.pdf)  
**作者**：Furkan Mumcu, Michael J. Jones, Anoop Cherian, Yasin Yilmaz  

**一句话要点**：提出基于多模态大语言模型描述活动的半监督视频异常检测框架，以提升复杂异常检测与可解释性。

**关键词**：视频异常检测, 多模态大语言模型, 半监督学习, 可解释性, 对象交互, 文本描述

## 3 点简述
- 现有半监督视频异常检测方法难以检测对象交互的复杂异常且缺乏可解释性。
- 利用MLLM生成对象活动与交互的文本描述，通过比较训练与测试视频描述检测异常。
- 在基准数据集上验证，有效检测交互异常并在无交互异常数据集上达到先进性能。

## 摘要（原文）

> Existing semi-supervised video anomaly detection (VAD) methods often struggle
> with detecting complex anomalies involving object interactions and generally
> lack explainability. To overcome these limitations, we propose a novel VAD
> framework leveraging Multimodal Large Language Models (MLLMs). Unlike previous
> MLLM-based approaches that make direct anomaly judgments at the frame level,
> our method focuses on extracting and interpreting object activity and
> interactions over time. By querying an MLLM with visual inputs of object pairs
> at different moments, we generate textual descriptions of the activity and
> interactions from nominal videos. These textual descriptions serve as a
> high-level representation of the activity and interactions of objects in a
> video. They are used to detect anomalies during test time by comparing them to
> textual descriptions found in nominal training videos. Our approach inherently
> provides explainability and can be combined with many traditional VAD methods
> to further enhance their interpretability. Extensive experiments on benchmark
> datasets demonstrate that our method not only detects complex interaction-based
> anomalies effectively but also achieves state-of-the-art performance on
> datasets without interaction anomalies.

