---
layout: default
title: MMFineReason: Closing the Multimodal Reasoning Gap via Open Data-Centric Methods
---

# MMFineReason: Closing the Multimodal Reasoning Gap via Open Data-Centric Methods
**arXiv**：[2601.21821v1](https://arxiv.org/abs/2601.21821) · [PDF](https://arxiv.org/pdf/2601.21821.pdf)  
**作者**：Honglin Lin, Zheng Liu, Yun Zhu, Chonghan Qin, Juekai Lin, Xiaoran Shang, Conghui He, Wentao Zhang, Lijun Wu  

**一句话要点**：提出MMFineReason数据集以解决开源视觉语言模型在高质量多模态推理数据上的不足

**关键词**：多模态推理, 数据集构建, 链式思维标注, 视觉语言模型, 参数效率, 数据蒸馏

## 3 点简述
- 开源视觉语言模型因缺乏高质量推理数据而落后于专有系统，尤其在STEM图表和视觉谜题等领域
- 通过三阶段流程构建大规模多模态推理数据集，包含1.8M样本和5.1B解决方案令牌，基于Qwen3-VL-235B-A22B-Thinking蒸馏高质量推理标注
- 微调模型在参数效率上表现优异，例如MMFineReason-4B超越Qwen3-VL-8B-Thinking，并发现仅7%数据子集可达到全数据集性能

## 摘要（原文）

> Recent advances in Vision Language Models (VLMs) have driven significant progress in visual reasoning. However, open-source VLMs still lag behind proprietary systems, largely due to the lack of high-quality reasoning data. Existing datasets offer limited coverage of challenging domains such as STEM diagrams and visual puzzles, and lack consistent, long-form Chain-of-Thought (CoT) annotations essential for eliciting strong reasoning capabilities. To bridge this gap, we introduce MMFineReason, a large-scale multimodal reasoning dataset comprising 1.8M samples and 5.1B solution tokens, featuring high-quality reasoning annotations distilled from Qwen3-VL-235B-A22B-Thinking. The dataset is established via a systematic three-stage pipeline: (1) large-scale data collection and standardization, (2) CoT rationale generation, and (3) comprehensive selection based on reasoning quality and difficulty awareness. The resulting dataset spans STEM problems, visual puzzles, games, and complex diagrams, with each sample annotated with visually grounded reasoning traces. We fine-tune Qwen3-VL-Instruct on MMFineReason to develop MMFineReason-2B/4B/8B versions. Our models establish new state-of-the-art results for their size class. Notably, MMFineReason-4B succesfully surpasses Qwen3-VL-8B-Thinking, and MMFineReason-8B even outperforms Qwen3-VL-30B-A3B-Thinking while approaching Qwen3-VL-32B-Thinking, demonstrating remarkable parameter efficiency. Crucially, we uncover a "less is more" phenomenon via our difficulty-aware filtering strategy: a subset of just 7\% (123K samples) achieves performance comparable to the full dataset. Notably, we reveal a synergistic effect where reasoning-oriented data composition simultaneously boosts general capabilities.

