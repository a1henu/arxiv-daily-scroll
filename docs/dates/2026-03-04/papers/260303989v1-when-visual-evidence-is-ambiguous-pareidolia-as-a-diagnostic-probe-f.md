---
layout: default
title: When Visual Evidence is Ambiguous: Pareidolia as a Diagnostic Probe for Vision Models
---

# When Visual Evidence is Ambiguous: Pareidolia as a Diagnostic Probe for Vision Models
**arXiv**：[2603.03989v1](https://arxiv.org/abs/2603.03989) · [PDF](https://arxiv.org/pdf/2603.03989.pdf)  
**作者**：Qianpu Chen, Derya Soydaner, Rob Saunders  

**一句话要点**：提出基于面孔幻觉的诊断框架，分析视觉模型在模糊证据下的解释机制与偏差

**关键词**：面孔幻觉诊断, 视觉模型评估, 语义鲁棒性, 不确定性分析, 视觉语言模型

## 3 点简述
- 核心问题：视觉模型如何解释模糊的面孔幻觉图像，涉及检测、定位、不确定性和偏差
- 方法要点：引入表示层诊断框架，统一评估六种模型，涵盖视觉语言模型、纯视觉分类和检测模型
- 实验或效果：揭示三种解释机制，如视觉语言模型的语义过度激活和检测模型的保守抑制，显示不确定性与偏差解耦

## 摘要（原文）

> When visual evidence is ambiguous, vision models must decide whether to interpret face-like patterns as meaningful. Face pareidolia, the perception of faces in non-face objects, provides a controlled probe of this behavior. We introduce a representation-level diagnostic framework that analyzes detection, localization, uncertainty, and bias across class, difficulty, and emotion in face pareidolia images. Under a unified protocol, we evaluate six models spanning four representational regimes: vision-language models (VLMs; CLIP-B/32, CLIP-L/14, LLaVA-1.5-7B), pure vision classification (ViT), general object detection (YOLOv8), and face detection (RetinaFace). Our analysis reveals three mechanisms of interpretation under ambiguity. VLMs exhibit semantic overactivation, systematically pulling ambiguous non-human regions toward the Human concept, with LLaVA-1.5-7B producing the strongest and most confident over-calls, especially for negative emotions. ViT instead follows an uncertainty-as-abstention strategy, remaining diffuse yet largely unbiased. Detection-based models achieve low bias through conservative priors that suppress pareidolia responses even when localization is controlled. These results show that behavior under ambiguity is governed more by representational choices than score thresholds, and that uncertainty and bias are decoupled: low uncertainty can signal either safe suppression, as in detectors, or extreme over-interpretation, as in VLMs. Pareidolia therefore provides a compact diagnostic and a source of ambiguity-aware hard negatives for probing and improving the semantic robustness of vision-language systems. Code will be released upon publication.

