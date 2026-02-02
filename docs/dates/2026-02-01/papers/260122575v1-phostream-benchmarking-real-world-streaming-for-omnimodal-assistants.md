---
layout: default
title: PhoStream: Benchmarking Real-World Streaming for Omnimodal Assistants in Mobile Scenarios
---

# PhoStream: Benchmarking Real-World Streaming for Omnimodal Assistants in Mobile Scenarios
**arXiv**：[2601.22575v1](https://arxiv.org/abs/2601.22575) · [PDF](https://arxiv.org/pdf/2601.22575.pdf)  
**作者**：Xudong Lu, Huankang Guan, Yang Bo, Jinpeng Chen, Xintong Guo, Shuhan Li, Fang Liu, Peiwen Sun, Xueying Li, Wei Zhang, Xue Yang, Rui Liu, Hongsheng Li  

**一句话要点**：提出PhoStream基准以评估移动场景中多模态大语言模型的实时流处理能力

**关键词**：流式多模态基准, 移动助手评估, 实时音频-视觉理解, 开放式问答, LLM-as-a-Judge

## 3 点简述
- 核心问题：现有基准在移动助手连续音频-视觉流处理及时响应方面存在不足
- 方法要点：构建首个移动中心流基准，统一屏上屏下场景，支持开放式问答与自动生成验证
- 实验或效果：模型在即时和回溯任务表现良好，但前向任务得分低，揭示响应时机决策缺陷

## 摘要（原文）

> Multimodal Large Language Models excel at offline audio-visual understanding, but their ability to serve as mobile assistants in continuous real-world streams remains underexplored. In daily phone use, mobile assistants must track streaming audio-visual inputs and respond at the right time, yet existing benchmarks are often restricted to multiple-choice questions or use shorter videos. In this paper, we introduce PhoStream, the first mobile-centric streaming benchmark that unifies on-screen and off-screen scenarios to evaluate video, audio, and temporal reasoning. PhoStream contains 5,572 open-ended QA pairs from 578 videos across 4 scenarios and 10 capabilities. We build it with an Automated Generative Pipeline backed by rigorous human verification, and evaluate models using a realistic Online Inference Pipeline and LLM-as-a-Judge evaluation for open-ended responses. Experiments reveal a temporal asymmetry in LLM-judged scores (0-100): models perform well on Instant and Backward tasks (Gemini 3 Pro exceeds 80), but drop sharply on Forward tasks (16.40), largely due to early responses before the required visual and audio cues appear. This highlights a fundamental limitation: current MLLMs struggle to decide when to speak, not just what to say. Code and datasets used in this work will be made publicly accessible at https://github.com/Lucky-Lance/PhoStream.

