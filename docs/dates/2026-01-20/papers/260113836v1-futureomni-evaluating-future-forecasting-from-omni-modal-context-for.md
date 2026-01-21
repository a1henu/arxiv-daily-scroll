---
layout: default
title: FutureOmni: Evaluating Future Forecasting from Omni-Modal Context for Multimodal LLMs
---

# FutureOmni: Evaluating Future Forecasting from Omni-Modal Context for Multimodal LLMs
**arXiv**：[2601.13836v1](https://arxiv.org/abs/2601.13836) · [PDF](https://arxiv.org/pdf/2601.13836.pdf)  
**作者**：Qian Chen, Jinlan Fu, Changsong Li, See-Kiong Ng, Xipeng Qiu  

**一句话要点**：提出FutureOmni基准以评估多模态大语言模型从视听环境预测未来事件的能力

**关键词**：未来预测, 多模态基准, 视听推理, 指令调优, 全模态模型

## 3 点简述
- 核心问题：现有基准主要关注回顾性理解，缺乏对多模态大语言模型未来预测能力的评估
- 方法要点：通过可扩展的LLM辅助、人机协作流程构建基准，包含919个视频和1,034个多选题对
- 实验或效果：评估13个全模态和7个纯视频模型，最佳准确率64.8%，并设计OFF训练策略提升性能

## 摘要（原文）

> Although Multimodal Large Language Models (MLLMs) demonstrate strong omni-modal perception, their ability to forecast future events from audio-visual cues remains largely unexplored, as existing benchmarks focus mainly on retrospective understanding. To bridge this gap, we introduce FutureOmni, the first benchmark designed to evaluate omni-modal future forecasting from audio-visual environments. The evaluated models are required to perform cross-modal causal and temporal reasoning, as well as effectively leverage internal knowledge to predict future events. FutureOmni is constructed via a scalable LLM-assisted, human-in-the-loop pipeline and contains 919 videos and 1,034 multiple-choice QA pairs across 8 primary domains. Evaluations on 13 omni-modal and 7 video-only models show that current systems struggle with audio-visual future prediction, particularly in speech-heavy scenarios, with the best accuracy of 64.8% achieved by Gemini 3 Flash. To mitigate this limitation, we curate a 7K-sample instruction-tuning dataset and propose an Omni-Modal Future Forecasting (OFF) training strategy. Evaluations on FutureOmni and popular audio-visual and video-only benchmarks demonstrate that OFF enhances future forecasting and generalization. We publicly release all code (https://github.com/OpenMOSS/FutureOmni) and datasets (https://huggingface.co/datasets/OpenMOSS-Team/FutureOmni).

