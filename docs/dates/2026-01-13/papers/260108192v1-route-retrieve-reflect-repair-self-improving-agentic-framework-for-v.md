---
layout: default
title: Route, Retrieve, Reflect, Repair: Self-Improving Agentic Framework for Visual Detection and Linguistic Reasoning in Medical Imaging
---

# Route, Retrieve, Reflect, Repair: Self-Improving Agentic Framework for Visual Detection and Linguistic Reasoning in Medical Imaging
**arXiv**：[2601.08192v1](https://arxiv.org/abs/2601.08192) · [PDF](https://arxiv.org/pdf/2601.08192.pdf)  
**作者**：Md. Faiyaz Abdullah Sayeedi, Rashedur Rahman, Siam Tahsin Bhuiyan, Sefatul Wasi, Ashraful Islam, Saadia Binte Alam, AKM Mahbubur Rahman  

**一句话要点**：提出R^4框架以提升医学影像中视觉检测与语言推理的可靠性和空间定位能力

**关键词**：医学影像分析, 视觉语言模型, 代理框架, 弱监督检测, 报告生成, 自我改进

## 3 点简述
- 医学影像分析中现有视觉语言模型多为单次黑箱，缺乏对推理、安全性和空间定位的控制
- R^4框架通过路由、检索、反思和修复四个代理协同工作，分解并优化影像分析流程
- 在胸部X光分析实验中，无需梯度微调即显著提升报告生成和弱监督检测性能

## 摘要（原文）

> Medical image analysis increasingly relies on large vision-language models (VLMs), yet most systems remain single-pass black boxes that offer limited control over reasoning, safety, and spatial grounding. We propose R^4, an agentic framework that decomposes medical imaging workflows into four coordinated agents: a Router that configures task- and specialization-aware prompts from the image, patient history, and metadata; a Retriever that uses exemplar memory and pass@k sampling to jointly generate free-text reports and bounding boxes; a Reflector that critiques each draft-box pair for key clinical error modes (negation, laterality, unsupported claims, contradictions, missing findings, and localization errors); and a Repairer that iteratively revises both narrative and spatial outputs under targeted constraints while curating high-quality exemplars for future cases. Instantiated on chest X-ray analysis with multiple modern VLM backbones and evaluated on report generation and weakly supervised detection, R^4 consistently boosts LLM-as-a-Judge scores by roughly +1.7-+2.5 points and mAP50 by +2.5-+3.5 absolute points over strong single-VLM baselines, without any gradient-based fine-tuning. These results show that agentic routing, reflection, and repair can turn strong but brittle VLMs into more reliable and better grounded tools for clinical image interpretation. Our code can be found at: https://github.com/faiyazabdullah/MultimodalMedAgent

