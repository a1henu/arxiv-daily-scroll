---
layout: default
title: CP-Env: Evaluating Large Language Models on Clinical Pathways in a Controllable Hospital Environment
---

# CP-Env: Evaluating Large Language Models on Clinical Pathways in a Controllable Hospital Environment
**arXiv**：[2512.10206v1](https://arxiv.org/abs/2512.10206) · [PDF](https://arxiv.org/pdf/2512.10206.pdf)  
**作者**：Yakun Zhu, Zhongzhen Huang, Qianhan Feng, Linjie Mu, Yannian Gu, Shaoting Zhang, Qi Dou, Xiaofan Zhang  

**一句话要点**：提出CP-Env可控医院环境以评估大语言模型在端到端临床路径中的表现

**关键词**：临床路径评估, 可控医院环境, 大语言模型, 端到端模拟, 医疗AI代理

## 3 点简述
- 当前基准在动态临床场景中评估大语言模型不足，CP-Env模拟医院生态系统支持分支长程任务执行
- CP-Env采用三层评估框架涵盖临床效能、流程能力和专业伦理，揭示模型在路径复杂性中易产生幻觉
- 实验显示过度推理步骤可能适得其反，顶级模型通过知识内化减少工具依赖，提供基准和工具促进医疗AI发展

## 摘要（原文）

> Medical care follows complex clinical pathways that extend beyond isolated physician-patient encounters, emphasizing decision-making and transitions between different stages. Current benchmarks focusing on static exams or isolated dialogues inadequately evaluate large language models (LLMs) in dynamic clinical scenarios. We introduce CP-Env, a controllable agentic hospital environment designed to evaluate LLMs across end-to-end clinical pathways. CP-Env simulates a hospital ecosystem with patient and physician agents, constructing scenarios ranging from triage and specialist consultation to diagnostic testing and multidisciplinary team meetings for agent interaction. Following real hospital adaptive flow of healthcare, it enables branching, long-horizon task execution. We propose a three-tiered evaluation framework encompassing Clinical Efficacy, Process Competency, and Professional Ethics. Results reveal that most models struggle with pathway complexity, exhibiting hallucinations and losing critical diagnostic details. Interestingly, excessive reasoning steps can sometimes prove counterproductive, while top models tend to exhibit reduced tool dependency through internalized knowledge. CP-Env advances medical AI agents development through comprehensive end-to-end clinical evaluation. We provide the benchmark and evaluation tools for further research and development at https://github.com/SPIRAL-MED/CP-Env.

