---
layout: default
title: User Prompting Strategies and Prompt Enhancement Methods for Open-Set Object Detection in XR Environments
---

# User Prompting Strategies and Prompt Enhancement Methods for Open-Set Object Detection in XR Environments
**arXiv**：[2601.23281v1](https://arxiv.org/abs/2601.23281) · [PDF](https://arxiv.org/pdf/2601.23281.pdf)  
**作者**：Junfeng Lin, Yanming Xiu, Maria Gorlatova  

**一句话要点**：提出用户提示策略与增强方法以提升XR环境中开放集目标检测的鲁棒性

**关键词**：开放集目标检测, XR环境, 用户提示策略, 提示增强, 视觉语言模型, 鲁棒性评估

## 3 点简述
- 研究开放集目标检测在XR环境中用户提示模糊、不明确或过于详细时的性能问题
- 通过模拟用户提示行为评估模型，并应用提示增强策略改善性能
- 实验显示提示增强在模糊提示下显著提升性能，mIoU增益超55%

## 摘要（原文）

> Open-set object detection (OSOD) localizes objects while identifying and rejecting unknown classes at inference. While recent OSOD models perform well on benchmarks, their behavior under realistic user prompting remains underexplored. In interactive XR settings, user-generated prompts are often ambiguous, underspecified, or overly detailed. To study prompt-conditioned robustness, we evaluate two OSOD models, GroundingDINO and YOLO-E, on real-world XR images and simulate diverse user prompting behaviors using vision-language models. We consider four prompt types: standard, underdetailed, overdetailed, and pragmatically ambiguous, and examine the impact of two enhancement strategies on these prompts. Results show that both models exhibit stable performance under underdetailed and standard prompts, while they suffer degradation under ambiguous prompts. Overdetailed prompts primarily affect GroundingDINO. Prompt enhancement substantially improves robustness under ambiguity, yielding gains exceeding 55% mIoU and 41% average confidence. Based on the findings, we propose several prompting strategies and prompt enhancement methods for OSOD models in XR environments.

