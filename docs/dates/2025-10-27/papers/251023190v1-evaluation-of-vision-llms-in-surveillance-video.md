---
layout: default
title: Evaluation of Vision-LLMs in Surveillance Video
---

# Evaluation of Vision-LLMs in Surveillance Video
**arXiv**：[2510.23190v1](https://arxiv.org/abs/2510.23190) · [PDF](https://arxiv.org/pdf/2510.23190.pdf)  
**作者**：Pascal Benschop, Cristian Meo, Justin Dauwels, Jelte P. Mense  

**一句话要点**：评估视觉-语言模型在监控视频中的零样本异常检测能力

**关键词**：视觉-语言模型, 零样本学习, 异常检测, 监控视频, 空间推理, 隐私保护

## 3 点简述
- 核心问题：监控视频数据量庞大，需自动检测异常事件以提升公共安全。
- 方法要点：将视频转为文本描述，通过文本蕴含评分实现零样本异常识别。
- 实验效果：在UCF-Crime和RWF-2000数据集上测试，隐私过滤可能降低准确性。

## 摘要（原文）

> The widespread use of cameras in our society has created an overwhelming
> amount of video data, far exceeding the capacity for human monitoring. This
> presents a critical challenge for public safety and security, as the timely
> detection of anomalous or criminal events is crucial for effective response and
> prevention. The ability for an embodied agent to recognize unexpected events is
> fundamentally tied to its capacity for spatial reasoning. This paper
> investigates the spatial reasoning of vision-language models (VLMs) by framing
> anomalous action recognition as a zero-shot, language-grounded task, addressing
> the embodied perception challenge of interpreting dynamic 3D scenes from sparse
> 2D video. Specifically, we investigate whether small, pre-trained vision--LLMs
> can act as spatially-grounded, zero-shot anomaly detectors by converting video
> into text descriptions and scoring labels via textual entailment. We evaluate
> four open models on UCF-Crime and RWF-2000 under prompting and
> privacy-preserving conditions. Few-shot exemplars can improve accuracy for some
> models, but may increase false positives, and privacy filters -- especially
> full-body GAN transforms -- introduce inconsistencies that degrade accuracy.
> These results chart where current vision--LLMs succeed (simple, spatially
> salient events) and where they falter (noisy spatial cues, identity
> obfuscation). Looking forward, we outline concrete paths to strengthen spatial
> grounding without task-specific training: structure-aware prompts, lightweight
> spatial memory across clips, scene-graph or 3D-pose priors during description,
> and privacy methods that preserve action-relevant geometry. This positions
> zero-shot, language-grounded pipelines as adaptable building blocks for
> embodied, real-world video understanding. Our implementation for evaluating
> VLMs is publicly available at:
> https://github.com/pascalbenschopTU/VLLM_AnomalyRecognition

