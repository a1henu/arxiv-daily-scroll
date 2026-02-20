---
layout: default
title: MedClarify: An information-seeking AI agent for medical diagnosis with case-specific follow-up questions
---

# MedClarify: An information-seeking AI agent for medical diagnosis with case-specific follow-up questions
**arXiv**：[2602.17308v1](https://arxiv.org/abs/2602.17308) · [PDF](https://arxiv.org/pdf/2602.17308.pdf)  
**作者**：Hui Min Wong, Philip Heesen, Pascal Janetzky, Martin Bendszus, Stefan Feuerriegel  

**一句话要点**：提出MedClarify AI代理，通过生成针对性随访问题以支持医疗诊断决策。

**关键词**：医疗诊断, AI代理, 随访问题生成, 信息论推理, 鉴别诊断

## 3 点简述
- 核心问题：医疗大语言模型在生成信息性随访问题以推理鉴别诊断方面能力不足。
- 方法要点：基于信息论计算候选诊断并主动生成问题以减少不确定性。
- 实验或效果：相比单次推理基线，减少诊断错误约27个百分点。

## 摘要（原文）

> Large language models (LLMs) are increasingly used for diagnostic tasks in medicine. In clinical practice, the correct diagnosis can rarely be immediately inferred from the initial patient presentation alone. Rather, reaching a diagnosis often involves systematic history taking, during which clinicians reason over multiple potential conditions through iterative questioning to resolve uncertainty. This process requires considering differential diagnoses and actively excluding emergencies that demand immediate intervention. Yet, the ability of medical LLMs to generate informative follow-up questions and thus reason over differential diagnoses remains underexplored. Here, we introduce MedClarify, an AI agent for information-seeking that can generate follow-up questions for iterative reasoning to support diagnostic decision-making. Specifically, MedClarify computes a list of candidate diagnoses analogous to a differential diagnosis, and then proactively generates follow-up questions aimed at reducing diagnostic uncertainty. By selecting the question with the highest expected information gain, MedClarify enables targeted, uncertainty-aware reasoning to improve diagnostic performance. In our experiments, we first demonstrate the limitations of current LLMs in medical reasoning, which often yield multiple, similarly likely diagnoses, especially when patient cases are incomplete or relevant information for diagnosis is missing. We then show that our information-theoretic reasoning approach can generate effective follow-up questioning and thereby reduces diagnostic errors by ~27 percentage points (p.p.) compared to a standard single-shot LLM baseline. Altogether, MedClarify offers a path to improve medical LLMs through agentic information-seeking and to thus promote effective dialogues with medical LLMs that reflect the iterative and uncertain nature of real-world clinical reasoning.

