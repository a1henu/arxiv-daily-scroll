---
layout: default
title: Enhancing LLM-based Autonomous Driving with Modular Traffic Light and Sign Recognition
---

# Enhancing LLM-based Autonomous Driving with Modular Traffic Light and Sign Recognition
**arXiv**：[2511.14391v1](https://arxiv.org/abs/2511.14391) · [PDF](https://arxiv.org/pdf/2511.14391.pdf)  
**作者**：Fabian Schmidt, Noushiq Mohammed Kayilan Abdul Nazar, Markus Enzweiler, Abhinav Valada  

**一句话要点**：提出TLS-Assist模块以增强LLM自动驾驶中的交通灯和标志识别能力

**关键词**：自动驾驶, 交通灯识别, 交通标志识别, 模块化冗余, LLM增强, 安全关键检测

## 3 点简述
- LLM自动驾驶代理缺乏强制交通规则机制，难以可靠检测小物体如交通灯和标志
- TLS-Assist将检测转换为结构化自然语言消息，注入LLM输入以增强安全关注
- 在CARLA的LangAuto基准测试中，驾驶性能提升达14%，交通违规减少

## 摘要（原文）

> Large Language Models (LLMs) are increasingly used for decision-making and planning in autonomous driving, showing promising reasoning capabilities and potential to generalize across diverse traffic situations. However, current LLM-based driving agents lack explicit mechanisms to enforce traffic rules and often struggle to reliably detect small, safety-critical objects such as traffic lights and signs. To address this limitation, we introduce TLS-Assist, a modular redundancy layer that augments LLM-based autonomous driving agents with explicit traffic light and sign recognition. TLS-Assist converts detections into structured natural language messages that are injected into the LLM input, enforcing explicit attention to safety-critical cues. The framework is plug-and-play, model-agnostic, and supports both single-view and multi-view camera setups. We evaluate TLS-Assist in a closed-loop setup on the LangAuto benchmark in CARLA. The results demonstrate relative driving performance improvements of up to 14% over LMDrive and 7% over BEVDriver, while consistently reducing traffic light and sign infractions. We publicly release the code and models on https://github.com/iis-esslingen/TLS-Assist.

