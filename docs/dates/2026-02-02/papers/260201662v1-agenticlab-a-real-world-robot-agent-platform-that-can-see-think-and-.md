---
layout: default
title: AgenticLab: A Real-World Robot Agent Platform that Can See, Think, and Act
---

# AgenticLab: A Real-World Robot Agent Platform that Can See, Think, and Act
**arXiv**：[2602.01662v1](https://arxiv.org/abs/2602.01662) · [PDF](https://arxiv.org/pdf/2602.01662.pdf)  
**作者**：Pengyuan Guo, Zhonghao Mai, Zhengtong Xu, Kaidi Zhang, Heng Zhang, Zichen Miao, Arash Ajoudani, Zachary Kingston, Qiang Qiu, Yu She  

**一句话要点**：提出AgenticLab平台以评估真实世界中基于视觉语言模型的机器人代理能力

**关键词**：机器人代理平台, 视觉语言模型, 真实世界操作, 闭环评估, 非结构化环境

## 3 点简述
- 核心问题：现有视觉语言模型在非结构化环境中长时程闭环操作能力不明确，缺乏可比较的评估平台
- 方法要点：开发模型无关的机器人代理平台，集成感知、任务分解、在线验证和重规划闭环流程
- 实验或效果：在真实机器人任务中基准测试先进代理，揭示离线测试未捕捉的失败模式如多步接地一致性问题

## 摘要（原文）

> Recent advances in large vision-language models (VLMs) have demonstrated generalizable open-vocabulary perception and reasoning, yet their real-robot manipulation capability remains unclear for long-horizon, closed-loop execution in unstructured, in-the-wild environments. Prior VLM-based manipulation pipelines are difficult to compare across different research groups' setups, and many evaluations rely on simulation, privileged state, or specially designed setups. We present AgenticLab, a model-agnostic robot agent platform and benchmark for open-world manipulation. AgenticLab provides a closed-loop agent pipeline for perception, task decomposition, online verification, and replanning. Using AgenticLab, we benchmark state-of-the-art VLM-based agents on real-robot tasks in unstructured environments. Our benchmark reveals several failure modes that offline vision-language tests (e.g., VQA and static image understanding) fail to capture, including breakdowns in multi-step grounding consistency, object grounding under occlusion and scene changes, and insufficient spatial reasoning for reliable manipulation. We will release the full hardware and software stack to support reproducible evaluation and accelerate research on general-purpose robot agents.

