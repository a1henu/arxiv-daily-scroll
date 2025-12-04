---
layout: default
title: Rethinking Prompt Design for Inference-time Scaling in Text-to-Visual Generation
---

# Rethinking Prompt Design for Inference-time Scaling in Text-to-Visual Generation
**arXiv**：[2512.03534v1](https://arxiv.org/abs/2512.03534) · [PDF](https://arxiv.org/pdf/2512.03534.pdf)  
**作者**：Subin Kim, Sangwoo Mo, Mamshad Nayeem Rizve, Yiran Xu, Difan Liu, Jinwoo Shin, Tobias Hinz  

**一句话要点**：提出PRIS框架，通过推理时自适应重设计提示以提升文本到视觉生成的对齐效果。

**关键词**：文本到视觉生成, 推理时扩展, 提示重设计, 元素级对齐评估, 视觉生成优化

## 3 点简述
- 核心问题：文本到视觉生成中，固定提示导致视觉生成扩展时质量停滞，难以精确对齐用户意图。
- 方法要点：PRIS框架在推理时审查生成视觉，识别失败模式，并基于元素级事实校正重设计提示以改进生成。
- 实验或效果：在文本到图像和视频基准测试中有效，如VBench 2.0提升15%，验证联合扩展提示与视觉的关键性。

## 摘要（原文）

> Achieving precise alignment between user intent and generated visuals remains a central challenge in text-to-visual generation, as a single attempt often fails to produce the desired output. To handle this, prior approaches mainly scale the visual generation process (e.g., increasing sampling steps or seeds), but this quickly leads to a quality plateau. This limitation arises because the prompt, crucial for guiding generation, is kept fixed. To address this, we propose Prompt Redesign for Inference-time Scaling, coined PRIS, a framework that adaptively revises the prompt during inference in response to the scaled visual generations. The core idea of PRIS is to review the generated visuals, identify recurring failure patterns across visuals, and redesign the prompt accordingly before regenerating the visuals with the revised prompt. To provide precise alignment feedback for prompt revision, we introduce a new verifier, element-level factual correction, which evaluates the alignment between prompt attributes and generated visuals at a fine-grained level, achieving more accurate and interpretable assessments than holistic measures. Extensive experiments on both text-to-image and text-to-video benchmarks demonstrate the effectiveness of our approach, including a 15% gain on VBench 2.0. These results highlight that jointly scaling prompts and visuals is key to fully leveraging scaling laws at inference-time. Visualizations are available at the website: https://subin-kim-cv.github.io/PRIS.

